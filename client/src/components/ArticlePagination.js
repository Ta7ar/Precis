import { Pagination, PaginationItem, PaginationLink } from "reactstrap";

const ArticlePagination = (props) => {
  const { currentPage, setPage, pages } = props;
  return (
    <Pagination style={{ marginBottom: "2rem" }}>
      {Array(pages)
        .fill(0)
        .map((_, i) => {
          const page = i + 1;
          return (
            <PaginationItem active={currentPage === page}>
              <PaginationLink onClick={() => setPage(page)}>
                {page}
              </PaginationLink>
            </PaginationItem>
          );
        })}
    </Pagination>
  );
};

export default ArticlePagination;
