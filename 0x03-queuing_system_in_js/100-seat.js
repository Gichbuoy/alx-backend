import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const app = express();
const port = 1245;
const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);
const queue = kue.createQueue();

const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  return await getAsync('available_seats');
};

let reservationEnabled = true;

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      console.error('Reservation failed');
      return res.json({ status: 'Reservation failed' });
    }
    console.log(`Seat reservation job ${job.id} completed`);
    res.json({ status: 'Reservation in process' });
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();
    if (currentSeats <= 0) {
      reservationEnabled = false;
      console.error(`Seat reservation job ${job.id} failed: Not enough seats available`);
      return done(new Error('Not enough seats available'));
    }
    await reserveSeat(currentSeats - 1);
    if (currentSeats === 1) {
      reservationEnabled = false;
    }
    console.log(`Seat reservation job ${job.id} completed`);
    done();
  });
});

export default app;
