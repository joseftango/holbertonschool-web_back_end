import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userPro = signUpUser(firstName, lastName);
  const photoRej = uploadPhoto(fileName);
  return Promise.allSettled([userPro, photoRej]);
}
