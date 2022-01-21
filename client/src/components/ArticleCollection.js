import React, { useState, useEffect } from "react";
import Article from "./Article";
import { Spinner } from "reactstrap";

const ArticleCollection = () => {
  const [articlesData, setArticlesData] = useState(null);

  useEffect(() => {
    fetch("/api")
      .then((res) => res.json())
      .then((data) => setArticlesData(data));
  }, []);

  return (
    <div>
      {!articlesData && (
        <div
          style={{
            padding: "1rem",
            display: "flex",
            alignItems: "center",
            gap: "1rem",
          }}
        >
          Loading Articles <Spinner color="primary" type="grow" />
        </div>
      )}
      {articlesData &&
        articlesData.articles.map((article, i) => <Article>{article}</Article>)}
    </div>
  );
};

export default ArticleCollection;
