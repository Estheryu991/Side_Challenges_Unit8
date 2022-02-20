# You're given with 1000 records of GAM products, with associated data. Among these 1000 records, we know that 30 are defectuous, but we don't know which ones. Your goal is to find the indices of these products.
# The submission format is an ordered list of 30 indices, such as [0, 1, 2, 3, 4, 56, 57, 58, 59, 60, 61, 111, 112, 113, 114, 115, 116, 117, 228, 229, 270, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999]

# Get the data needed for the challenge Quality Assurance using
# requests.get(
#   'https://hackathon.unit8.com/api/get_resource',
#   headers={'Authorization': 'Token 61259af05fdbca4da869e4838b15dc2cccbc53f7'},
#   json={'challenge_id': 5}
# )
# As every API call, it returns a JSON you can read using response.json()

# Submit your solution to the challenge Quality Assurance using
# requests.post(
#   'https://hackathon.unit8.com/api/submit',
#   headers={'Authorization': 'Token 61259af05fdbca4da869e4838b15dc2cccbc53f7'},
#   json={'challenge_id': 5, 'submission': YOUR_SUBMISSION}
# )
