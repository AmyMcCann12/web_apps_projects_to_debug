from lib.post import Post


class PostRepository:
    def __init__(self):
        self.store = []

    def all(self):
        return self.store

    def all_by_tag(self, tag):
        #post_list =[]
        #for post in self.store:
        #    for posttag in post.tags:
         #       if tag in posttag:
        #            post_list.append(post)
        #return post_list
        return[post for post in self.store if tag in post.tags]

        

    def create(self, post):
        post.id = self._generate_next_id()
        self.store.append(post)
        return post

    def _generate_next_id(self):
        if len(self.store)>0:

            return max([post.id for post in self.store]) + 1
        else:
            return 1
