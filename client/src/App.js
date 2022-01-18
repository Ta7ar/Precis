import Navbar from "./components/Navbar";
import About from "./components/About";
import { Container } from "reactstrap";
import { Route, Switch, Redirect } from "react-router-dom";
function App() {
  return (
    <div className="App">
      <Navbar />
      <Container fluid="md">
        <Switch>
          <Route path="/about" exact>
            <About />
          </Route>
          <Route path="/" exact>
            <div>Home</div>
          </Route>
          <Route path="/">
            <Redirect to="/" />
          </Route>
        </Switch>
      </Container>
    </div>
  );
}

export default App;
