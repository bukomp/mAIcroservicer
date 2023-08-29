import readline from 'readline';
import { keepAlive } from './utils/keepalive';
import { randomInt } from 'crypto';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

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
  rl.on('line', (input: string) => {
    const [command, ...args] = input.trim().split(' ');
    switch (command) {
      case 'generate':
        const [min, max, count] = args.map(Number);
        console.log(generateRandomNumbers(min, max, count));
        break;
      case 'exit':
        console.log('Goodbye!');
        process.exit(0); // Exit the process when 'exit' command is received
        break;
      default:
        console.log(
          'Unknown command. Type "generate min max count" to generate random numbers.'
        );
    }
  });

  console.log(
    "CLI App started. Type 'generate min max count' to generate random numbers."
  );
};

main();
