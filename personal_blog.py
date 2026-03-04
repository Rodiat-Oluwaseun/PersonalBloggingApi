class BlogRepository(DatabaseConnection):
    def fetch_all_posts(self):
        try:
            conn = self.get_connection()
            cur = conn.cursor(dictionary=True)
            cur.execute("SELECT id, title, content, created_at FROM posts")
            rows = cur.fetchall()
            cur.close()
            conn.close()
            return rows
        except Error as e:
            # Re-raising for the API layer to handle
            raise Exception(f"Database error: {str(e)}")

    def add_post(self, title, content):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
        conn.commit()
        new_id = cur.lastrowid
        cur.close()
        conn.close()
        return new_id
