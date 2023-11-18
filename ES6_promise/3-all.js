import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      const { body } = values[0];
      const { firstName } = values[1];
      const { lastName } = values[1];
      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch(() => {
      console.error('Signup system offline');
    });
}
