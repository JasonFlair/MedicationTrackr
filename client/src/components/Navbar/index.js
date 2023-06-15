import React, { useEffect, useState } from "react";
import {
  Nav,
  NavbarContainer,
  NavLogo,
  MobileIcon,
  NavMenu,
  NavItem,
  NavLinks,
  NavBtn,
  NavBtnLink,
  UtilsLinks,
} from "./NavbarElements";
import { FaBars } from "react-icons/fa";
import { IconContext } from "react-icons/lib";
import { animateScroll as scroll } from "react-scroll";

const Navbar = ({ toggle, isAuthenticated }) => {
  const [scrollNav, setScrollNav] = useState(false);

  const changeNav = () => {
    if (window.scrollY >= 80) {
      setScrollNav(true);
    } else {
      setScrollNav(false);
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", changeNav);
  }, []);

  const toggleHome = () => {
    scroll.scrollToTop();
  };

  return (
    <>
      <IconContext.Provider value={{ color: "#fff" }}>
        <Nav scrollNav={scrollNav}>
          <NavbarContainer>
            <NavLogo to="/" onClick={toggleHome}>
              MedicationTrackr
            </NavLogo>
            <MobileIcon onClick={toggle}>
              <FaBars />
            </MobileIcon>
            <NavMenu>
              <NavItem key="services">
                <NavLinks
                  to="services"
                  smooth={true}
                  duration={500}
                  spy={true}
                  exact="true"
                  offset={-80}
                >
                  How it works
                </NavLinks>
              </NavItem>
              {/* <NavItem key="discover">
                <NavLinks
                  to="discover"
                  smooth={true}
                  duration={500}
                  spy={true}
                  exact="true"
                  offset={-80}
                >
                  Discover
                </NavLinks>
              </NavItem> */}
              {/* <NavItem key="services">
                <NavLinks
                  to="services"
                  smooth={true}
                  duration={500}
                  spy={true}
                  exact="true"
                  offset={-80}
                >
                  Services
                </NavLinks>
              </NavItem> */}
              {/* {[
                { to: 'about', title: 'About', }, 
                { to: 'discover', title: 'Discover', }, 
                { to: 'services', title: 'Services', },
              ].map(({ to, title }) => (
                <NavItem key={to}>
                  <NavLinks 
                    to={to}
                    smooth={true}
                    duration={500}
                    spy={true}
                    exact="true"
                    offset={-80}
                  >
                    {title}
                  </NavLinks>
                </NavItem>
              ))} */}
              {!isAuthenticated && (
                <UtilsLinks to="/register">Sign Up</UtilsLinks>
              )}
              {isAuthenticated && (
                <UtilsLinks to="/dose">My Medicines</UtilsLinks>
              )}
            </NavMenu>
            <NavBtn>
              {!isAuthenticated && <NavBtnLink to="/login">Sign In</NavBtnLink>}
              {isAuthenticated && <UtilsLinks to="/logout">Logout</UtilsLinks>}
            </NavBtn>
          </NavbarContainer>
        </Nav>
      </IconContext.Provider>
    </>
  );
};

export default Navbar;
