const textarea = document.querySelector("#commentForm");

textarea.addEventListener("keydown", function (event) {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    document.getElementById("commentForm").submit();
  }
});
console.log("this a test");
function LoadComments() {
  fetch("/about/", { headers: { "x-requested-with": "XMLHttpRequest" } })
    .then((response) => response.json())
    .then((data) => {
      const CommentsBox = document.getElementById("comments-box");
      CommentsBox.innerHTML = ""; // پاک کردن نظرات قبلی

      data.forEach((comment) => {
        const commentElement = document.createElement("p");
        commentElement.innerHTML = `<strong>کاربر ${comment.user}</strong>: ${comment.text}`;
        CommentsBox.appendChild(commentElement);
      });
    })
    .catch((error) => console.error("Error fetching comments:", error));
}

document.getElementById("commentForm").addEventListener("submit", function (e) {
  e.preventDefault(); // جلوگیری از رفرش صفحه

  const formData = new FormData(this);

  fetch("/about/", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((newComment) => {
      if (newComment.error) {
        console.error(newComment.error);
        return;
      }

      // افزودن نظر جدید به کامنت‌باکس
      const CommentsBox = document.getElementById("comments-box");
      const commentElement = document.createElement("p");
      commentElement.innerHTML = `<strong>کاربر ${newComment.user}</strong>: ${newComment.text}`;
      CommentsBox.prepend(commentElement); // اضافه کردن نظر به ابتدای لیست
      this.reset(); // پاک کردن فرم
    })
    .catch((error) => console.error("Error submitting comment:", error));
});

document.addEventListener("DOMContentLoaded", LoadComments);
