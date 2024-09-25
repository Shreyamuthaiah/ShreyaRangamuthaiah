# Aspiring Data Scientist

I’m an experienced software engineer and aspiring data scientist with a strong background in cloud computing, machine learning, and data science. Through hands-on experience in deploying AI solutions, automating workflows, and optimizing cloud infrastructure, I’ve developed a passion for leveraging data to solve complex problems. With a history of implementing data-driven systems that enhance operational efficiency, I’m excited to contribute to projects that require both technical expertise and a problem-solving mindset. 

As I work towards becoming a full-fledged data scientist, I focus on mastering key areas such as machine learning algorithms, data wrangling, data interpretation, and model deployment. I am enthusiastic about collaborating on projects that foster innovation, optimize processes, and unlock value from data. Driven by curiosity and a desire to learn, I am eager to contribute to the data science community and help organizations harness the power of data to make informed, strategic decisions.


## Education					       		
- M.Eng., Industrial Informatics	| Hochschule Emden/Leer | Emden, Germany (_August 2024_)	 			        		
- B.Eng., Electrical and Electronics | Sri Venkatashwara College of Engineering | Bengaluru, India (_August 2020_)

## Work Experience
**Intern - Procure, Contract and Facility Management IT | Deutsche Boerse | Eschborn, Germany (_March 2024 - August 2024_)**
- Implemented Google Document AI to process and extract data from approximately 60,000 invoices annually, significantly improving operational efficiency and streamlining business processes.
- Utilized machine learning algorithms, natural language processing (NLP), and optical character recognition (OCR) to automate data extraction, classification, and validation, increasing data accuracy and processing efficiency.
- Developed and deployed a Document AI system that increased invoice processing speed by 20%, enhanced workflow efficiency, and improved data accuracy to 93% by optimizing the automation process for high-volume invoice processing.

**Intern - Enterprise Analytics IT | Deutsche Boerse | Eschborn, Germany (_September 2023 - February 2024_)**
- Analyzed project data to design and implement a comprehensive data visualization dashboard using business intelligence (BI) tools, improving budget management, transparency, and enabling more informed decision-making within project timelines.
- Managed administrative tasks and system performance in SAP Analytics Cloud, ensuring efficient data handling, reliability, and performance for business intelligence operations.
- Developed and launched a website using GitHub Pages to create a centralized hub for team insights, enhancing communication, collaboration, and project coordination.

**Associate Professional Software Engineer | DXC Technology | Bengaluru, India (_June 2020 - August 2022_)**
- Successfully migrated 120 critical Linux servers to FMO via TMO, achieving a 15% reduction in downtime and significantly improving system reliability and performance.
- Conducted VMware replication tasks using VSphere and Double Take, achieving a 98% success rate for V2V (Virtual-to-Virtual), P2P (Physical-to-Physical), and P2V (Physical-to-Virtual) migrations, ensuring minimal disruption during server transitions.
- Proactively troubleshot and resolved critical issues during cutover windows, resulting in a 99% seamless server handover rate and maintaining operational continuity.
- Deployed and configured Amazon EC2 and Azure VMs across various operating systems (Linux, CentOS, Ubuntu, RHEL), optimizing cloud infrastructure and enhancing system performance.
- Established and managed a Single Source of Truth (SSoT) data repository for all source workloads, increasing data accuracy and collection efficiency by 25%, leading to more reliable analytics and decision-making.

## Projects
### Master Thesis:  Optimizing Vendor Invoice Processes: A Document AI approach for efficient management

This project proposes a transformative approach to revolutionize traditional invoice management processes. Existing manual workflows are often error-prone and time-consuming, negatively impacting payment efficiency. By integrating Artificial Intelligence (AI) into the conventional Vendor Invoice Management (VIM) system utilized in SAP, aimed to significantly reduce the time required for invoice preparation, field extraction, and overall processing. This enhancement will lead to improved efficiency in payment processing.

The project leverages the capabilities of Google Cloud Platform (GCP) to seamlessly integrate AI technologies, creating a streamlined and accelerated invoicing process. Utilizing Google Document AI, implemented a pretrained model with Generative AI capabilities, which minimizes the need for extensive training while maximizing accuracy in invoice recognition and data extraction. The adoption of AI in invoice processing promises substantial time savings of about 20% for invoice processing and 93% of model accuracy for extracting data.

![Optimizing Vendor Invoice Process](/assets/images/MT_SS.png)

### Bachelor Thesis: Automatized Perambulator for Disabled Person
[Publication](https://www.irjet.net/archives/V7/i5/IRJET-V7I5191.pdf)

This project introduces a smart wheelchair designed to improve the independence of individuals with disabilities by integrating head and hand gesture recognition, voice commands, and GPS tracking. The wheelchair is equipped with ultrasonic sensors for automatic obstacle detection, a WiFi module, and an LDR for lighting control, all managed through the Blynk application. The integration of these technologies allows for seamless navigation and enhanced safety, making day-to-day activities more manageable for users.

The voice recognition system, powered by IFTTT, simplifies control, enabling users to operate the wheelchair with minimal physical effort. With real-time connectivity and automatic obstacle detection, this smart wheelchair not only increases mobility but also enhances safety and convenience, empowering users to lead more autonomous lives.

![Automatized Perambulator](/assets/images/BT_BD.png)


### Slope Control of a mobile robot using Arduino NiclaVision

Mobile robots have become an integral part of daily life, and improving their efficiency is critical to maximizing their utility. A key aspect of enhancing mobile robots involves obstacle detection and collision avoidance, enabling them to safely navigate their environments. This project focuses on classifying obstacles such as objects, slopes, and ditches to ensure smooth movement. Using Arduino Nicla Vision for real-time environment detection, the robot can respond dynamically to various terrain challenges.

To further enhance the robot's capabilities, supervised linear regression was employed using TensorFlow to predict the slope of the mobile robot. This approach allows the robot to better understand and react to inclines and declines in its path, improving navigation. By integrating machine learning with robotics, this project demonstrates a valuable application of data-driven insights to optimize mobile robot performance.

![Mobile robot slope detection](/assets/images/MR.png)
![State of Art](/assets/images/SOA.png)


### Smart Extruder – Industry 4.0 Component

The project aims to establish a communication interface for a smart extruder that allows seamless data exchange and visualization on a user-friendly interface. In line with Industry 4.0 (I4.0) standards, the smart extruder integrates with flexible production systems using a standardized interface for real-time control via EtherCAT. Additionally, smart sensors provide enhanced functionality, while MQTT is implemented as a communication protocol to support M2M communication and IoT platforms, even in limited infrastructures.

A Raspberry Pi microcontroller is used to control the stepper motor and handle data acquisition. The system publishes key data points like stepper drive speed, temperature, and fan speed through an MQTT broker. For data visualization, Grafana is utilized to display real-time data, allowing users to monitor performance and make informed decisions. This scalable and flexible communication system lays the groundwork for future production environments in line with I4.0 principles.

![Smart Extruder](/assets/images/SE.png)

### Optimization of Data Flow in the Production Environment

This project focuses on optimizing data flow in a production environment by analyzing large volumes of machine-generated data. Data from machines, collected in CSV files, will be processed using Apache Spark, which is connected to a MySQL database for seamless integration with Microsoft Power BI for visualization. By leveraging these technologies, the system enables efficient data analysis and provides actionable insights to enhance decision-making.

The solution aims to reduce the manual effort required for data processing and reporting while providing real-time visibility into machine performance. With optimized data flow, the project improves efficiency, supports management reporting, and delivers a scalable solution that can be integrated into existing production systems to promote overall operational growth and success.

![Pipeline](/assets/images/PP.png)


### Sea Level Predictor

This project involved analyzing a dataset of global average sea level changes since 1880 to predict sea level rise through the year 2050. Pandas was used to import and process data from a CSV file, followed by visualization using Matplotlib to create a scatter plot with Year on the x-axis and CSIRO Adjusted Sea Level on the y-axis.

To predict future sea level trends, the linregress function from Scipy.stats was applied to calculate the slope and y-intercept of the line of best fit, extending the projection through 2050. Additionally, a second line of best fit was plotted using data from the year 2000 onward to account for recent trends. This work demonstrates expertise in data visualization, regression analysis, and predictive modeling, highlighting the ability to extract valuable insights from complex datasets.

![Sea level predictor](/assets/images/SLP.png)

### Page View Time Series Visualiser

This project involved visualizing time series data to analyze the page views on the freeCodeCamp.org forum from May 2016 to December 2019. Pandas, Matplotlib, and Seaborn were utilized to create multiple visualizations, allowing for the identification of trends and patterns in yearly and monthly page view growth.

The dataset was first cleaned by removing outliers, specifically filtering out days with page views in the top and bottom 2.5%. A line chart was then created using Matplotlib to visualize the daily page views over time. Additionally, a bar chart was generated to display the average daily page views for each month, grouped by year, providing insight into seasonal trends. Finally, two adjacent box plots were drawn using Seaborn to show the distribution of page views, both year-wise (to highlight trends) and month-wise (to observe seasonality).


### Medical data visualization

This project analyzed a medical dataset to explore the relationship between cardiovascular disease, body measurements, blood markers, and lifestyle choices. Key tasks included adding a BMI-based "overweight" column, normalizing cholesterol and glucose data, and cleaning the dataset by removing incorrect or extreme values.

Visualizations were created using Seaborn to show counts of lifestyle and medical factors for patients with and without cardiovascular disease. Additionally, a correlation matrix was generated to identify relationships between variables like blood pressure, cholesterol, and cardiovascular risk. This project highlights expertise in data preprocessing, feature engineering, and visualization using Pandas, Matplotlib, and Seaborn.



## Publications
1. Talebi S., Lary D.J., Wijeratne L. OH., and Lary, T. Modeling Autonomic Pupillary Responses from External Stimuli Using Machine Learning (2019). DOI: 10.26717/BJSTR.2019.20.003446
2. Wijeratne, L.O.; Kiv, D.R.; Aker, A.R.; Talebi, S.; Lary, D.J. Using Machine Learning for the Calibration of Airborne Particulate Sensors. Sensors 2020, 20, 99.
3. Lary, D.J.; Schaefer, D.; Waczak, J.; Aker, A.; Barbosa, A.; Wijeratne, L.O.H.; Talebi, S.; Fernando, B.; Sadler, J.; Lary, T.; Lary, M.D. Autonomous Learning of New Environments with a Robotic Team Employing Hyper-Spectral Remote Sensing, Comprehensive In-Situ Sensing and Machine Learning. Sensors 2021, 21, 2240. https://doi.org/10.3390/s21062240
4. Zhang, Y.; Wijeratne, L.O.H.; Talebi, S.; Lary, D.J. Machine Learning for Light Sensor Calibration. Sensors 2021, 21, 6259. https://doi.org/10.3390/s21186259
5. Talebi, S.; Waczak, J.; Fernando, B.; Sridhar, A.; Lary, D.J. Data-Driven EEG Band Discovery with Decision Trees. Preprints 2022, 2022030145 (doi: 10.20944/preprints202203.0145.v1).
6. Fernando, B.A.; Sridhar, A.; Talebi, S.; Waczak, J.; Lary, D.J. Unsupervised Blink Detection Using Eye Aspect Ratio Values. Preprints 2022, 2022030200 (doi: 10.20944/preprints202203.0200.v1).
7. Talebi, S. et al. Decoding Physical and Cognitive Impacts of PM Concentrations at Ultra-fine Scales, 29 March 2022, PREPRINT (Version 1) available at Research Square [https://doi.org/10.21203/rs.3.rs-1499191/v1]
8. Lary, D.J. et al. (2022). Machine Learning, Big Data, and Spatial Tools: A Combination to Reveal Complex Facts That Impact Environmental Health. In: Faruque, F.S. (eds) Geospatial Technology for Human Well-Being and Health. Springer, Cham. https://doi.org/10.1007/978-3-030-71377-5_12
9. Wijerante, L.O.H. et al. (2022). Advancement in Airborne Particulate Estimation Using Machine Learning. In: Faruque, F.S. (eds) Geospatial Technology for Human Well-Being and Health. Springer, Cham. https://doi.org/10.1007/978-3-030-71377-5_13

- [Data Science Blog](https://medium.com/@shawhin)
