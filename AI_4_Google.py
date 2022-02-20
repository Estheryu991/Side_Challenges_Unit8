# To be Continued...

#Google Side Challenge 

# GAM Pharma recently heard of a condition named Diabetic Retinopathy (diabetes complication that affects the eyesight). You're provided with a tabular dataset labeled either 1 or 0, depending on whether the patient has the condition (1) or not (0).
# GAM Pharma wants you to accurately predict unlabeled records. The goal of this challenge is to get the model with the highest accuracy.
# The resource (given with the get_resource endpoint) contains a train (labeled) dataset and a test (unlabeled) dataset. Getting the resource to the correct format might be slightly harder than during the previous challenges. It's part of it, so... good luck with that! :p

# The Data
# The data consists of 18 features for each patient:
# 1) The binary result of pre-screening, where 1 indicates severe retinal abnormality and 0 its lack.
# 2-7) The results of MA detection. Each feature value stands for the number of MAs found at the confidence levels alpha = 0.5, . . . , 1, respectively.
# 8-15) contain the same information as 2-7) for exudates. However, as exudates are represented by a set of points rather than the number of pixels constructing the lesions, these features are normalized by dividing the number of lesions with the diameter of the ROI to compensate for different image sizes.
# 16) The euclidean distance of the center of the macula and the center of the optic disc to provide important information regarding the patient’s condition. This feature is also normalized with the diameter of the ROI.
# 17) The diameter of the optic disc.
# 18) The binary result of the AM/FM-based classification.
# Further, the training data also contains a feature called ‘Class’, where 1 = contains signs of DR and 0 = does not contain signs of DR.

# The results will be communicated after the code freeze. Your submission must follow the format {patient_id: has_condition [...]} for all of the 230 records of the test dataset. For instance: {126: 0, 930: 0, 51: 1 [...]}

# Get the data needed for the challenge AI for good using
# requests.get(
#   'https://hackathon.unit8.com/api/get_resource',
#   headers={'Authorization': 'Token 61259af05fdbca4da869e4838b15dc2cccbc53f7'},
#   json={'challenge_id': 2}
# )
# As every API call, it returns a JSON you can read using response.json()

# Submit your solution to the challenge AI for good using
# requests.post(
#   'https://hackathon.unit8.com/api/submit',
#   headers={'Authorization': 'Token 61259af05fdbca4da869e4838b15dc2cccbc53f7'},
#   json={'challenge_id': 2, 'submission': YOUR_SUBMISSION}
# )
