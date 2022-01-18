import React from "react";

const About = () => {
  return (
    <div>
      <section style={{ borderBottom: "1px dashed grey" }}>
        <h4>About</h4>
        <p>
          Precis scrapes frontpage news articles from news sites and summarizes
          them into 5 sentences using Natural Language Processing.
        </p>
      </section>
      <br />
      <section style={{ borderBottom: "1px dashed grey" }}>
        <h4>Disclaimer</h4>
        <p>
          Rights to all scraped articles belong to their respective publishers.
        </p>
      </section>
      <br />
      <section>
        <h4>Contributing</h4>
        <p>
          Want to see articles from more publishers? Other ideas to improve the
          app? <a href="https://github.com/Ta7ar/Precis">Contribute!</a>
        </p>
      </section>
    </div>
  );
};

export default About;
