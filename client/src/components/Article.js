import React from "react";
import { Card, CardBody, CardTitle, CardText, CardFooter } from "reactstrap";
import CNBC from "./../logos/CNBC.svg";
import CBS from "./../logos/CBS News.svg";

const logos = {
  CNBC,
  CBS,
};

const Article = (props) => {
  const { title, publisher, body, link } = props.children;
  const publisherLogo = logos[publisher];
  return (
    <Card style={{ marginBottom: "1em" }}>
      <CardBody>
        <CardTitle tag="h6" style={{ fontWeight: "600" }}>
          {title} |
          <img
            src={publisherLogo}
            height="20px"
            style={{ padding: "0 0.5em" }}
          />
        </CardTitle>
        <CardText>{body}</CardText>
      </CardBody>
      <CardFooter>
        <sub style={{ bottom: "0" }}>
          Full Article Link: <a href={link}>{link}</a>
        </sub>
      </CardFooter>
    </Card>
  );
};

export default Article;
