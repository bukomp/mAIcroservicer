import supertest from 'supertest';
import app from '../src/app';
import { afterAll, expect, test } from '@jest/globals';

const api = supertest(app);

test('GET /api/test', async () => {
  const response = await api.get('/api/test').expect(200);
  expect(response.body).toEqual({ message: 'Connection Test' });
});
test('GET /api/range', async () => {
  const response = await api
    .get('/api/range')
    .query({ min: 1, max: 10, number: 5 });
  expect(response.status).toBe(500);
  expect(response.body).toBeInstanceOf(Object);
});

afterAll((done) => {
  app.close(done);
});
