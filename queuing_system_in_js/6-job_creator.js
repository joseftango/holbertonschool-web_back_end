const kue = require('kue');

const queue = kue.createQueue();

const pushNotificationJobType = 'push_notification_code';

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const pushNotificationJob = queue.create(pushNotificationJobType, jobData)
  .priority('high')
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${pushNotificationJob.id}`);
    } else {
      console.error('Notification job failed:', err);
    }
    queue.shutdown(5000, (err) => {
      console.log('Queue connection closed');
      process.exit(0);
    });
  });

pushNotificationJob.on('complete', () => {
  console.log('Notification job completed');
});

pushNotificationJob.on('failed', (err) => {
  console.error('Notification job failed:', err);
});

process.on('SIGTERM', () => {
  queue.shutdown(5000, (err) => {
    console.log('Queue connection closed on process exit');
    process.exit(0);
  });
});