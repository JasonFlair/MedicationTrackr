import React from "react";
import {
  ServicesContainer,
  ServicesH1,
  ServicesWrapper,
  ServicesCard,
  ServicesIcon,
  ServicesH2,
  ServicesP,
} from "./ServicesElements";
import Icon1 from "../../images/signup.PNG";
import Icon2 from "../../images/dashboard.PNG";
import Icon3 from "../../images/email.jpg";

const Services = () => {
  return (
    <ServicesContainer id="services">
      <ServicesH1>How It Works</ServicesH1>
      <ServicesWrapper>
        <ServicesCard>
          <ServicesIcon src={Icon1} />
          <ServicesH2>Sign up with a username:</ServicesH2>
          <ServicesP>
            To begin using MedicationTrackr, sign up with a unique username.
            Your username will serve as your identifier within the app.
          </ServicesP>
        </ServicesCard>
        <ServicesCard>
          <ServicesIcon src={Icon2} />
          <ServicesH2>Add medicine details to the dashboard:</ServicesH2>
          <ServicesP>
            Once signed in, access the dashboard where you can manage your
            medication regimen. Add details of the medicine you need to track,
            including its name, quantity per dose, frequency (number of times
            per day), and the duration for which the medicine needs to be taken.
            The dashboard provides an intuitive interface for easily entering
            and updating medication information.
          </ServicesP>
        </ServicesCard>
        <ServicesCard>
          <ServicesIcon src={Icon3} />
          <ServicesH2>Receive personalized email reminders:</ServicesH2>
          <ServicesP>
            MedicationTrackr leverages a personalized notification system to
            send you timely email reminders about taking your medications. These
            reminders aim to ensure you adhere to your prescribed medication
            regimen and stay on track with your treatment. With
            MedicationTrackr's user-friendly interface and personalized email
            reminders, managing your medications becomes more efficient and
            convenient. Stay organized, never miss a dose, and enhance your
            overall medication adherence for better health and well-being
          </ServicesP>
        </ServicesCard>
      </ServicesWrapper>
    </ServicesContainer>
  );
};

export default Services;
