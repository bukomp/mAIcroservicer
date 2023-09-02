if (process.env.NODE_ENV !== 'production') {
  const { config } = require('dotenv');
  config();
}

const config = {
  PIPE: process.env.PIPE,
  NODE_ENV: process.env.NODE_ENV,
  //DATABASE_URL: process.env.DATABASE_URL,
  //JWT_SECRET: process.env.JWT_SECRET,
};

console.log(config);
export default config;
