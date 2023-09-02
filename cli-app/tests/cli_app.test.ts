import { exec } from 'child_process';
import { expect, describe, test } from '@jest/globals';

describe('CLI App', () => {
  test('should return error when less than 3 arguments are provided', (done) => {
    exec('node ./dist/cli.js 1 2', (error, stdout, stderr) => {
      expect(stdout).toContain(
        'Please provide min, max and count as arguments.'
      );
      done();
    });
  });

  test('should generate random numbers when min, max and count are provided', (done) => {
    exec('node ./dist/cli.js 1 10 5', (error, stdout, stderr) => {
      expect(stdout.split(',').length).toEqual(5);
      done();
    });
  });
});
