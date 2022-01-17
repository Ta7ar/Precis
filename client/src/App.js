import Navbar from "./components/Navbar";
import About from "./components/About";
import { Container } from "reactstrap";
function App() {
  return (
    <div className="App">
      <Navbar />
      <Container fluid="md">
        <About />
      </Container>
    </div>
  );
}

export default App;
