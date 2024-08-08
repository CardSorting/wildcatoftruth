class Beatmap:
    def __init__(self, data):
        """
        Initializes a new beatmap from the provided data.
        :param data: A list of tuples where each tuple represents a note in the format (time_ms, lane_index).
        """
        self.notes = sorted(data, key=lambda x: x[0])  # Ensure notes are sorted by time
        self.current_note_index = 0
        self.total_notes = len(self.notes)

    def get_next_note_timing(self, current_time):
        """
        Retrieves the next note timing and lane index based on the current time.
        :param current_time: The current time in the game.
        :return: A tuple of (time_ms, lane_index) if there's a next note, or None if all notes are processed.
        """
        if self.current_note_index < self.total_notes and current_time >= self.notes[self.current_note_index][0]:
            note_timing, lane_index = self.notes[self.current_note_index]
            self.current_note_index += 1
            return note_timing, lane_index
        return None

    def reset(self):
        """
        Resets the beatmap to start from the beginning.
        """
        self.current_note_index = 0