import express, { Request, Response } from 'express';
import config from './utils/config';
import cliRouter from './controllers/cli.controller';

const app = express();
const PORT = config.PORT || 3000;

app.use(express.json());

app.get('/', (req: Request, res: Response) => {
  res.send('Hello World!');
});

app.use('/api', cliRouter);

const server = app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

export default server;
