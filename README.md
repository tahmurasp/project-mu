# Methodist University AI Assistant (Trial Version)

Welcome to the **Methodist University AI Assistant**, a cutting-edge tool developed to enhance the academic advising experience for students and faculty. This trial version demonstrates how AI can streamline academic processes and provide personalized support.

Built using **Streamlit**, the AI Assistant features an interactive interface that allows students and faculty to engage seamlessly. The assistant processes and retrieves data from academic documents, such as university guidelines and course schedules, by utilizing the **PyPDF2** library for PDF parsing. Advanced natural language processing is powered by **Langchain**'s integration with **OpenAI** and **Hugging Face** models, allowing for highly contextual and conversational interactions.

Crucial libraries like **FAISS** enable fast and efficient searches across embedded documents, while **ConversationalRetrievalChain** ensures the assistant remembers and uses previous context to provide accurate advice and support over the course of interactions.

This system offers data-driven insights into how students behave with the AI assistant versus traditional advising methods, empowering Methodist University to make personalized academic guidance more accessible, efficient, and impactful.
 

## Project Overview

This AI Assistant is designed to offer comprehensive support for academic-related tasks at Methodist University. It simplifies several aspects of the student and faculty experience:

- **Academic Advising**: Provides tailored recommendations based on each student's academic history, major, and preferences, ensuring optimal course selection and advising.
- **Personalized Course Planning**: Suggests courses that align with the student's academic path, future goals, and available schedules.
- **Program Exploration**: Helps students explore the various departments and majors available at Methodist University, guiding them toward programs that suit their interests and strengths.
- **Faculty Support Tools**: Allows faculty to track and advise students more effectively, using data-driven insights to guide their recommendations.
- **Data-Driven Insights**: Collects and analyzes how students interact with the system to improve future iterations of the tool.
- **Behavioral Analysis**: Compares student behaviors when using the AI tool versus more traditional "brute force" methods, providing insights for further system improvements.
- **Streamlined Scheduling**: Ensures that students are on track with their required courses, helping them avoid common scheduling conflicts and delays in graduation.
- **Administrative Efficiency**: Reduces the burden on faculty by automating many of the administrative tasks associated with academic advising.

## Key Features

- **AI-Powered Academic Assistance**: Uses artificial intelligence to offer customized advice and course recommendations based on each student's academic progress and goals.
  
- **Behavioral Data Analytics**: Tracks student interactions to identify patterns and compare them with traditional advising methods, helping to fine-tune the AI's suggestions.
  
- **Course Scheduling Optimization**: Assists students in building a balanced and conflict-free schedule by recommending courses that fit into their overall academic plan.
  
- **Interactive Department and Major Exploration**: Allows students to browse various departments and majors, exploring available programs, requirements, and opportunities at Methodist University.
  
- **Adaptive Learning Algorithms**: Continuously improves the quality of recommendations by learning from student behaviors and preferences, making the tool smarter with each interaction.
  
- **Faculty Dashboard**: Provides faculty with a dedicated interface to monitor student progress, streamline communication, and offer personalized guidance based on data analytics.
  
- **Seamless Integration with University Systems**: Syncs with the university’s existing academic systems and databases, ensuring that students and faculty always have access to the most up-to-date information.
  
- **User-Friendly Interface**: Designed with ease of use in mind, making it accessible to students of all technical backgrounds while enhancing user engagement.

- **Predictive Analytics**: Provides insights into future academic trends, helping students make informed decisions about their course selection and academic journey.

- **Flexible and Scalable**: This trial version is just the beginning, with future updates planned to add even more features, making it adaptable to evolving student needs.

## About Methodist University

Methodist University is renowned for its commitment to fostering academic excellence across various disciplines. With a strong focus on personalized learning, it offers a broad spectrum of majors and minors across diverse departments, including:

- **Computer Science**
- **Business Analytics**
- **Human Resource Management**
- **International Studies**
- **General Education Programs**
  
The AI Assistant integrates seamlessly with the academic framework of Methodist University, supporting the institution’s mission to empower students to achieve their academic and career goals.

## Future Development

This trial version represents just the beginning. Future iterations will incorporate even more advanced features, such as deeper behavioral analytics, improved natural language processing for more human-like interactions, and more robust scheduling tools.

## How to Start the Application

To run the Methodist University AI Assistant using Streamlit, follow these steps:

1. **Ensure All Dependencies Are Installed**: Before running the application, make sure all required libraries are installed as detailed in the previous sections.

2. **Navigate to the Project Directory**: Open your terminal or command prompt, and navigate to the root directory of the cloned repository:

   ```bash
   cd methodist-university-ai-assistant
   
3. **Run the Application**: Start the Streamlit app by executing the following command:

   ```bash
   streamlit run app.py
   
4. **Access the Application**: Once the application starts, Streamlit will provide a local URL (usually `http://localhost:8501`) in the terminal. Open this URL in your web browser to interact with the AI Assistant.


