import React from 'react';
import HeroSection from '../components/HeroSection'; 
import InfoSection from '../components/InfoSection';
import {
  homeObjeOne, 
  homeObjeTwo,
} from '../components/InfoSection/Data';
import Services from '../components/Services';

const Home = ({isAuthenticated}) => {
  return (
    <>
      <HeroSection isAuthenticated={isAuthenticated}/>
      {/* <InfoSection {...homeObjeOne} /> */}
      {/* <InfoSection {...homeObjeTwo} /> */}
      <Services />
    </>
  );
};

export default Home;
