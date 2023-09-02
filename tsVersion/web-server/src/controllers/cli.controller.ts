import util from 'util';
const exec = util.promisify(require('node:child_process').exec);

import express from 'express';
const router = express.Router();

router.get('/test', async (req, res) => {
  try {
    const { stdout, stderr } = await exec('echo Connection Test');
    if (stderr) {
      res.status(500).send({ error: stderr });
      return;
    }
    res.send({ message: stdout.trim() });
  } catch (error) {
    res.status(500).send({ error: (error as Error).message });
  }
});

router.get('/range', async (req, res) => {
  const min = Number(req.query.min);
  const max = Number(req.query.max);
  const number = Number(req.query.number);

  if (!min || !max || !number) {
    res
      .status(400)
      .send({ error: 'Please provide min, max and number parameters' });
    return;
  }

  if (number < min || number > max) {
    res.status(400).send({ error: 'Number is out of the provided range' });
    return;
  }

  await exec(
    'cli_app ' + min + ' ' + max + ' ' + number,
    (error: any, stdout: any, stderr: any) => {
      if (error || stderr) {
        res.status(500).send({ error: error.message });
        return;
      }
      res.send(`${stdout}`);
    }
  );
});

export default router;
