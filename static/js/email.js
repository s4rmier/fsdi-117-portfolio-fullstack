// This is executed when the user press "Send Email"

document
  .getElementById("emailform")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const form = event.target; // this is the element that is getting the submit action (the form)

    //get values
    const name = form.elements.name.value;
    const email = form.elements.email.value;
    const subject = form.elements.subject.value;
    const message = form.elements.message.value;

    // E-mail JS account
    // Add public key
    emailjs.init("Q6hVD575kSJHoLC1w");

    const params = {
      from_email: email,
      from_name: name,
      subject: subject,
      message: message,
    };

    // verify if the subject is empty
    if (!subject) {
      const result = confirm(
        "Subject is empty. Are you sure you want to send the email?"
      );
      if (result) {
        sendEmail();
      }
    } else {
      sendEmail();
    }

    function sendEmail() {
      // param 1 = service ID
      // param 2 = template ID

      emailjs.send("service_q2ckt05", "template_3shiaj5", params).then(
        function (response) {
          alert("Email was successfully sent");
          form.reset(); // clear the form
        },
        function (error) {
          alert("Error sending email");
        }
      );
    }
  });
