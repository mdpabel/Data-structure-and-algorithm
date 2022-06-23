const range = (start, end) => {
  let length = end - start + 1;

  return Array.from({ length }, (_, idx) => idx + start);
};

const usePagination = ({
  totalCount,
  pageSize,
  siblingCount = 1,
  currentPage,
}) => {
  const paginationRange = () => {
    const totalPageCount = Math.ceil(totalCount / pageSize);
    const totalPageNumbers = 5 + siblingCount;

    // case 1 : number of page we want to show is greater than the total number of page
    if (totalPageNumbers > totalPageCount) {
      return range(1, totalPageNumbers);
    }
    // Left & right sibling indices
    const leftSiblingIndex = currentPage - siblingCount;
    const rightSiblingIndex = currentPage + siblingCount;

    // Should show dots
    const shouldShowLeftDots = leftSiblingIndex > 3;
    const shouldShowRightDots = totalPageCount - 2 > rightSiblingIndex;

    const firstPageIndex = 1;
    const lastPageIndex = totalPageCount;

    // case 2 : No left dots to show, but rights dots to be shown
    if (!shouldShowLeftDots && shouldShowRightDots) {
      const totalLeftItems = 3 + 2 * siblingCount;
      const leftRange = range(1, totalLeftItems);

      return [...leftRange, DOTS, totalPageNumbers];
    }

    // case 3 : No right dots to show,
    if (shouldShowLeftDots && !shouldShowRightDots) {
      const totalRightItems = 3 + 2 * siblingCount;
      const rightRange = range(
        totalPageCount - totalRightItems + 1,
        totalPageCount
      );
      return [firstPageIndex, DOTS, ...rightRange];
    }

    // case 4: Both left & right dots to be shown
    if (shouldShowLeftDots && shouldShowRightDots) {
      const middleItems = range(leftSiblingIndex, rightSiblingIndex);
      return [firstPageIndex, DOT, ...middleItems, DOT, lastPageIndex];
    }
  };

  return paginationRange;
};

const data = {
  totalCount: 50,
  pageSize: 10,
  siblingCount: 1,
  currentPage: 1,
};

const paginationRange = usePagination(data);

console.log(paginationRange());
