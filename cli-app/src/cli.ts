import { randomInt } from 'crypto';
import { keepAlive } from './utils/keepalive';

const generateRandomNumbers = (
  min: number,
  max: number,
  count: number
): string => {
  let numbers = [];
  for (let i = 0; i < count; i++) {
    numbers.push(randomInt(min, max));
  }
  return numbers.join(',');
};

const main = () => {
  const args = process.argv.slice(2);
  if (args.length < 3) {
    console.log('Please provide min, max and count as arguments.');
    process.exit(1);
  }
  const [min, max, count] = args.map(Number);
  console.log(generateRandomNumbers(min, max, count));
};

main();
