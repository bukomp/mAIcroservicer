import util from 'util';
const exec = util.promisify(require('node:child_process').exec);

import express from 'express';
const router = express.Router();

router.get('/cli/test', (req, res) => {
  const { exec } = require('child_process');
  exec(
    "echo 'status' > my_pipe",
    (error: { message: any }, stdout: any, stderr: any) => {
      if (error) {
        console.log(`error: ${error.message}`);
        return;
      }
      if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
      }
      res.send(`stdout: ${stdout}`);
    }
  );
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
