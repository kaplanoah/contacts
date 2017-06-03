import secret
import facebook

graph = facebook.GraphAPI(secret.facebook_token)

friends = graph.get_object('%s/friends' % secret.facebook_user_id)

for friend in friends['data']:
    print friend['name']
