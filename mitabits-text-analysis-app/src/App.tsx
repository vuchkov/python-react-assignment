import React from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Navbar, Nav } from 'react-bootstrap';

import TextAnalysisPage from './views/TextAnalysisPage'
import SearchPage from './views/SearchPage'

import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';


const App: React.FC = () => {
  return (
    <Router>
      <Navbar bg="light">
        <Navbar.Brand href="/">
          <img
            src="https://mitabits.com/logo.png"
            height="40"
            alt="Mitabits"
          />
        </Navbar.Brand>
        <Nav className="mr-auto">
          <Nav.Link href="/">Text analysis</Nav.Link>
          <Nav.Link href="/search">Knowledge Base</Nav.Link>
        </Nav>
      </Navbar>

      <Switch>
        <Route exact path="/">
          <TextAnalysisPage />
        </Route>
        <Route path="/search">
          <SearchPage />
        </Route>
      </Switch>
    </Router>

  );
}

export default App;
