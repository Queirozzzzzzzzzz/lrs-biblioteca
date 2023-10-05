var modal = document.getElementById("id_book-modal");
var btn = document.getElementById("id_book_modal_button");
var span = document.getElementsByClassName("close")[0];
var book_title = document.getElementById("book-modal-title");
var book_author = document.getElementById("book-modal-author");
var book_synopsis = document.getElementById("book-modal-synopsis");
var book_release_date = document.getElementById("book-modal-release_date");
var book_is_available = document.getElementById("book-modal-is_available");

// Modal de Livro

// Abrir modal
function OpenBookModal(title, author, synopsis, release_date, is_available) {
  modal.style.display = "block";
  book_title.innerHTML = title;
  book_author.innerHTML = author;
  book_synopsis.innerHTML = synopsis;
  book_release_date.innerHTML = release_date;
  book_is_available.innerHTML = is_available;
}

// Fechar modal
span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}