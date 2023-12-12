<?php

// Set the recipient email address
$to = 'stillfindingmyself24@gmail.com';

// Get the form data
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

// Create the email header
$headers = "From: $name <$email>\r\n";
$headers .= "Reply-To: $email\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=ISO-8859-1\r\n";

// Create the email body
$body = "
<!DOCTYPE html>
<html>
<head>
<title>Contact Form Submission</title>
</head>
<body>
<h1>Contact Form Submission</h1>
<p>Name: $name</p>
<p>Email: $email</p>
<p>Message: $message</p>
</body>
</html>
";

// Send the email
$sent = mail($to, 'Contact Form Submission', $body, $headers);

// Check if the email was sent successfully
if ($sent) {
  // Success message
  echo '<p>Your message was sent successfully!</p>';
} else {
  // Error message
  echo '<p>There was an error sending your message.</p>';
}

?>
