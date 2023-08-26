import express from 'express';
const router = express.Router();

router.post('/cli/test', (req, res) => {
  // Handle the request here
  res.send('CLI test request received');
});

export default router;
