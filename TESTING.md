# you.i API

## Backend Testing

### Table of Contents
   -   [Code Validation](https://github.com/SamarZiadat/youi_drf_api/blob/main/TESTING.md#code-validation)
   -   [Automated Testing](https://github.com/SamarZiadat/youi_drf_api/blob/main/TESTING.md#automated-testing)
   -   [Manual Testing](https://github.com/SamarZiadat/youi_drf_api/blob/main/TESTING.md#manual-testing)

### Code Validation

#### PEP8

The you.i API has been developed with the [pylint](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html) and [black](https://black.readthedocs.io/en/stable/) GitPod extensions that provide formatting, linting and internal PEP8 validation tests. No problems or warnings were found at the end of the project.

### Automated Testing

20 automated tests have been written into the you.i API to test user story scenarios. Automated tests were created to cover the following apps: posts, events, comments, reviews, likes, bookmarks and profiles.

![Automated testing](https://res.cloudinary.com/ddsrnz9la/image/upload/v1697818524/Screenshot_2023-10-20_at_17.10.08_jabzqk.png)

### Manual Testing
I carried out the following additional manual tests:

**Profiles**

✓ Profile List can be ordered by posts_count in ascending order

✓ Profile List can be ordered by posts_count in descending order

✓ Profile List can be ordered by events_count in ascending order

✓ Profile List can be ordered by events_count in descending order

✓ Profile List can be ordered by followers_count in ascending order

✓ Profile List can be ordered by followers_count in descending order

✓ Profile List can be ordered by following_count in ascending order

✓ Profile List can be ordered by following_count in descending order

**Posts**

✓ Posts List can be ordered by comments_count in ascending order

✓ Posts List can be ordered by comments_count in descending order

✓ Posts List can be ordered by likes_count in ascending order

✓ Posts List can be ordered by likes_count in descending order

✓ Posts List can be searched by owner

✓ Posts List can be searched on by content 

✓ Posts List can be searched on by tag

**Events**

✓ Event List can be ordered by reviews_count in ascending order

✓ Event List can be ordered by reviews_count in descending order

✓ Event List can be ordered by bookmarks_count in ascending order

✓ Event List can be ordered by bookmarks_count in descending order

✓ Event List can be searched by owner

✓ Event List can be searched on by title 

✓ Event List can be searched on by tag

✓ Event List can be searched on by event_date 

✓ Event List can be filtered by category

**Comments**

✓ Comment List can be filtered by post

**Reviews**

✓ Review List can be filtered by event