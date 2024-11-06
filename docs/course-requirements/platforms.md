# Required Platforms and Access Setup

To complete the course exercises and build applications effectively, you will need access to specific platforms. This document outlines the necessary accounts and API keys or tokens required for each platform, organized into three sections: **LLMs**, **Cloud Compute Platforms**, and **Other** (for additional services like Twilio and GitHub).

## 1. LLM Platforms

In this section, we cover the required access for platforms that provide large language models (LLMs) and related resources.

### OpenAI Developer API Key

To access OpenAI’s models programmatically, you need an OpenAI API key. Follow these steps:

1. **Create an OpenAI Account**  
   Go to [OpenAI’s website](https://platform.openai.com/signup) to sign up.

2. **Generate an API Key**  
   - Log in and navigate to [API Keys](https://platform.openai.com/account/api-keys).
   - Click on **Create new secret key** to generate a new API key.
   - Copy and store the key securely, as it will be needed to authenticate with OpenAI’s API.

3. **Usage and Billing**  
   OpenAI offers a free trial, but be mindful of usage limits and potential charges.

### Hugging Face Token

To access Hugging Face’s models and datasets programmatically, you’ll need a Hugging Face access token.

1. **Create a Hugging Face Account**  
   Sign up at [Hugging Face’s website](https://huggingface.co/join).

2. **Generate an Access Token**  
   - Log in, go to **Settings**, and select **Access Tokens**.
   - Click **New token**, set a name (e.g., “Course Token”), choose “Read” for access level, and generate the token.
   - Copy and save the token for use with Hugging Face’s resources.

## 2. Cloud Compute Platforms

This section details required access for cloud-based compute resources.

### AWS (Amazon Web Services)

AWS will provide cloud resources for deploying and running applications at scale.

1. **Create an AWS Account**  
   Go to [AWS’s website](https://aws.amazon.com/) to create an account.

2. **Generate Access Keys**  
   - Log in to the AWS Management Console.
   - Navigate to **IAM (Identity and Access Management)** > **Users** and select your user.
   - Under **Security credentials**, click **Create access key**.
   - Copy and store your Access Key ID and Secret Access Key securely for connecting to AWS services.

3. **Free Tier Usage**  
   AWS offers a free tier for new users, which may be sufficient for many course exercises. Monitor usage to avoid unexpected charges.

## 3. Other Platforms

This section includes additional services needed for the course.

### Twilio (for WhatsApp Integration)

Twilio will enable WhatsApp access, allowing you to build and deploy chatbot applications.

1. **Create a Twilio Account**  
   Sign up at [Twilio’s website](https://www.twilio.com/).

2. **Generate an API Key for WhatsApp**  
   - After logging in, navigate to **Console** > **API Keys & Tokens**.
   - Click on **Create new API Key**, give it a name, and copy the SID and Secret.
   - Follow Twilio’s documentation to set up WhatsApp messaging capabilities, including linking your WhatsApp number.

3. **Free Trial**  
   Twilio offers a free trial with a small amount of credit, allowing you to experiment with WhatsApp API functionality. Be sure to check usage limits.

### GitHub (for Project Repository Management)

GitHub will be used to manage project files and collaborate on code.

1. **Create a GitHub Account**  
   Go to [GitHub’s website](https://github.com/) and sign up for an account if you don’t already have one.

2. **Set Up SSH Keys (Optional)**  
   To simplify authentication, you may want to set up SSH keys.
   - Follow the instructions in GitHub's documentation for [generating SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
   - Once set up, add the public key to your GitHub account under **Settings** > **SSH and GPG keys**.

3. **Forking and Cloning Repositories**  
   During the course, you will be working with GitHub repositories. Familiarize yourself with forking and cloning repositories to easily access course materials and project files.

---
