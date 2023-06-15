import React, { useState } from "react";
import { ToastContainer } from "react-toastify";
import "./App.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./pages";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Footer from "./components/Footer";
import Form from "./components/Form";
import Logout from "./components/Logout";
import MedicalDose from "./components/MedicalDose";

const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const toggle = () => setIsOpen(!isOpen);
  const handleLogout = () => {
    window.localStorage.clear();
    setIsAuthenticated(false)
  }
  return (
    <Router>
      <Sidebar isOpen={isOpen} toggle={toggle} />
      <Navbar toggle={toggle} isAuthenticated={isAuthenticated} />
      <Switch>
        <Route
          exact
          path="/"
          render={() => <Home isAuthenticated={isAuthenticated} />}
        />
        <Route
          exact
          path="/register"
          render={() => (
            <Form
              formType="Register"
              isAuthenticated={isAuthenticated}
              setIsAuthenticated={setIsAuthenticated}
            />
          )}
        />
        <Route
          exact
          path="/login"
          render={() => (
            <Form
              formType="login"
              isAuthenticated={isAuthenticated}
              setIsAuthenticated={setIsAuthenticated}
            />
          )}
        />
        <Route
          exact
          path="/logout"
          render={() => (
            <Logout
              isAuthenticated={isAuthenticated}
              logoutUser={handleLogout}
            />
          )}
        />
        <Route
          exact
          path="/dose"
          render={() => (
            <MedicalDose
              isAuthenticated={isAuthenticated}
              logoutUser={handleLogout}
            />
          )}
        />
      </Switch>
      <ToastContainer />
      <Footer />
    </Router>
  );
};

export default App;
