import Navbar from "./components/Navbar";
import About from "./components/About";
import { Container } from "reactstrap";
import { Route, Switch, Redirect } from "react-router-dom";
import ArticleCollection from "./components/ArticleCollection";
import DateDisplay from "./components/DateDisplay";

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
            <DateDisplay />
            <ArticleCollection />
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
