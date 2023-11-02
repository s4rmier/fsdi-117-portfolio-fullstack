let projects;

/* Getting the data */
fetch("../data/projects.json")
  .then((response) => {
    return response.json();
  })
  .then(createProjectCards);

/* Printing the data */
function createProjectCards(json) {
  projects = json;
  console.log(projects);

  const projectsListElement = document.getElementById("projects-list");

  projectsListElement.innerHTML = projects.map(
    (project) =>
      `<div class="project-card">
          <a href="${project.url}" target="_blank">
                <img src="${project.img}" alt="" />
                <p class="project-name">${project.name}</p>
                <p>
                    ${project.description}
                </p>
                <p><strong>${project.year}</strong></p>

                <div class="technologies center">
                ${project.technologies.map(
                  (technology) => `<label>${technology}</label>`
                )}
                </div>
            </a>
        </div>`
  );
}

let experience;

fetch("../data/experience.json")
  .then((response) => {
    return response.json();
  })
  .then(createExperienceCards);

function createExperienceCards(json) {
  experience = json;

  const experienceListElement = document.getElementById("experience-list");

  experienceListElement.innerHTML = experience.map(
    (exp) =>
      `<div class="experience-card">
        <p class="experience-name">${exp.entity}</p>
        <p>${exp.title}</p>
        <p>${exp.description}</p>
        <p><strong>${exp.period}</strong></p>
        <div class="technologies">
         ${exp.technologies.map((technology) => `<label>${technology}</label>`)}
        </div>
    </div>`
  );
}
