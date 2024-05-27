moderation_logs.py (Python):

import logging

class ModerationLogs:
    def __init__(self):
        self.logger = logging.getLogger('moderation_logs')
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        file_handler = logging.FileHandler('moderation_logs.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        
    def log_moderation_action(self, user_id, action, reason):
        self.logger.info(f'User ID: {user_id} - Action: {action} - Reason: {reason}')

# Usage example:
# moderation_logs = ModerationLogs()
# moderation_logs.log_moderation_action('12345', 'Ban', 'Repeated violations')