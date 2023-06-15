import React, { useState } from "react";
import {
  HeroBg,
  HeroContainer,
  VideoBg,
  HeroContent,
  HeroH1,
  HerorP,
  HeroBtnWrapper,
  ArrowForward,
  ArrowRight,
} from "./HeroElements";
import { Button } from "../ButtonElements";
import Video from "../../videos/video.mp4";

const HeroSection = ({ isAuthenticated }) => {
  const [hover, setHover] = useState(false);
  const onHover = () => setHover(!hover);

  return (
    <HeroContainer id="home">
      <HeroBg>
        <VideoBg autoPlay loop muted src={Video} type="video/mp4" />
      </HeroBg>
      <HeroContent>
        <HeroH1>Never Miss a Dose!</HeroH1>
        <HerorP>Effortlessly Manage Your Medications with MedTrackr</HerorP>
        {!isAuthenticated && (
          <>
            <HeroBtnWrapper>
              <Button
                to="/register"
                onMouseEnter={onHover}
                onMouseLeave={onHover}
                primary="true"
                dark="true"
              >
                Get started {hover ? <ArrowForward /> : <ArrowRight />}
              </Button>
            </HeroBtnWrapper>
          </>
        )}
      </HeroContent>
    </HeroContainer>
  );
};

export default HeroSection;
