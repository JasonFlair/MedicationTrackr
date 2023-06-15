import carSvg from '../../images/svg-1.svg';
import piggybankSvg from '../../images/piggybank.svg'; 
import secureDataSvg from '../../images/secure_data.svg';

export const homeObjeOne = {
  id: 'about', 
  lightBg: false, 
  lightText: true, 
  lightTextDesc: true, 
  topLine: '', 
  headline: 'Benefits:', 
  description: 'Stay on track with personalized medication reminders. Track your medication history and adherence Reduce the risk of running out of medication.', 
  buttonLabel: 'Get started', 
  imgStart: false, 
  img: carSvg, 
  alt: 'Car', 
  dark: true, 
  primary: true, 
  darkText: false,
  to: '/',
};

export const homeObjeTwo = {
  id: 'about', 
  lightBg: true, 
  lightText: false, 
  lightTextDesc: false, 
  topLine: '', 
  headline: 'Benefits:', 
  description: 'Stay on track with personalized medication reminders. Track your medication history and adherence Reduce the risk of running out of medication.', 
  buttonLabel: 'Learn more', 
  imgStart: true, 
  img: piggybankSvg, 
  alt: 'Piggybank', 
  dark: false, 
  primary: false, 
  darkText: true,
  to: '/',
};

export const homeObjeThree = {
  id: 'signup', 
  lightBg: true, 
  lightText: false, 
  lightTextDesc: false, 
  topLine: 'Join our team', 
  headline: 'Creating an accout is extremely easy', 
  description: 'Get everything set up and ready in under 10 minutes. All you need to do is add your information and you\'re ready to go. ',
  buttonLabel: 'Start now', 
  imgStart: false, 
  img: secureDataSvg, 
  alt: 'Secure data', 
  dark: false, 
  primary: false, 
  darkText: true,
  to: '/register',
};