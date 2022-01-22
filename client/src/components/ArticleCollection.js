import React, { useState, useEffect } from "react";
import Article from "./Article";
import ArticlePagination from "./ArticlePagination";
import { Spinner } from "reactstrap";

const ArticleCollection = () => {
  const [articlesData, setArticlesData] = useState(null);
  const [page, setPage] = useState(1);

  useEffect(() => {
    fetch(`/api/${page}`)
      .then((res) => res.json())
      .then((data) => setArticlesData(data));
  }, [page]);

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
      {articlesData && (
        <>
          {articlesData.articles.map((article, i) => (
            <Article key={i}>{article}</Article>
          ))}
          <ArticlePagination
            currentPage={page}
            setPage={setPage}
            pages={articlesData.pages}
          />
        </>
      )}
    </div>
  );
};

export default ArticleCollection;
