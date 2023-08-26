import readline from 'readline';
import { keepAlive } from './utils/keepalive';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

const main = () => {
  rl.on('line', (input: string) => {
    switch (input.trim()) {
      case 'hello':
        console.log('Hello, user!');
        break;
      case 'status':
        console.log('CLI App is running.');
        break;
      case 'help':
        console.log(`
Available commands:
- hello: Greets the user.
- status: Shows the CLI status.
- exit: Closes the CLI app.
              `);
        break;
      case 'exit':
        console.log('Goodbye!');
        process.exit(0); // Exit the process when 'exit' command is received
        break;

      default:
        console.log('Unknown command. Type "help" for a list of commands.');
    }
  });

  console.log("CLI App started. Type 'help' for a list of commands.");

  keepAlive();
};

main();
