import React, { useState, useEffect } from "react";
import Article from "./Article";

const ArticleCollection = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [articlesData, setArticlesData] = useState(null);

  useEffect(() => {
    fetch("/api?limit=5&offset=0")
      .then((res) => res.json())
      .then((data) => setArticlesData(data));
  }, []);

  useEffect(() => {
    if (articlesData) {
      setIsLoading(false);
    } else {
      setIsLoading(true);
    }
  }, [articlesData]);

  return (
    <div>
      {articlesData &&
        articlesData.articles.map((article, i) => <Article>{article}</Article>)}
    </div>
  );
};

export default ArticleCollection;
