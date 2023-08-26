export const keepAlive = (): void => {
  setInterval(() => {
    console.log('Keeping alive...');
  }, 1000 * 60 * 5); // Log every 5 minutes
};
