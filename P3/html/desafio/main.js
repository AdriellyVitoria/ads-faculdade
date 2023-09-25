const projetos_container = document.querySelector(".conteudo_links");

document.addEventListener('DOMContentLoaded', async () => {

    const repos_promisse = await fetch("https://api.github.com/users/AdriellyVitoria/repos");
    const repos = await repos_promisse.json();
    repos.forEach(repo => {
        projetos_container.innerHTML += 
        `<div class="card">
            <p>${repo.name}</p>
            <a href="${repo.html_url}" target="_blank">Link</a>
        </div>`
    })
})