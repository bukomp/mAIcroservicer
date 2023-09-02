if (process.env.NODE_ENV !== 'production') {
  const { config } = require('dotenv');
  config();
}

const config = {
  PORT: process.env.PORT,
  NODE_ENV: process.env.NODE_ENV,
  PIPE: process.env.PIPE,
  //DATABASE_URL: process.env.DATABASE_URL,
  //JWT_SECRET: process.env.JWT_SECRET,
};

export default config;
