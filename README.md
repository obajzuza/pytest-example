# pytest-example

## Project structure
There are two folders containing different types of tests - `ui_tests` and `api_tests`, so that they can be run with pytest separately.
Folder `ui_test` contains also model(s) for the tests, expecting new page models to inherit `BasePage`.

### ui-test gif

### API test cases

#### Test Cases: `test_get_verse`
Test cases covering different paths to access the resources, checking the whole content of the response.
TC_01 and TC_02 checks for different representations of the books.
TC_03 checks if a desired translation can be chosen.

| Test Case ID | Path                         | Expected Content (bytes)                                                                                                                                                                                                                                                                 |
|--------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC_01        | gen 1:1                      | {"reference":"Genesis 1:1","verses":[{"book_id":"GEN","book_name":"Genesis","chapter":1,"verse":1,"text":"In the beginning, God created the heavens and the earth.\n"}],"text":"In the beginning, God created the heavens and the earth.\n","translation_id":"web","translation_name":"World English Bible","translation_note":"Public Domain"} |
| TC_02        | genesis 1:1                  | {"reference":"Genesis 1:1","verses":[{"book_id":"GEN","book_name":"Genesis","chapter":1,"verse":1,"text":"In the beginning, God created the heavens and the earth.\n"}],"text":"In the beginning, God created the heavens and the earth.\n","translation_id":"web","translation_name":"World English Bible","translation_note":"Public Domain"} |
| TC_03        | gen 1:1?translation=darby    | {"reference":"Genesis 1:1","verses":[{"book_id":"GEN","book_name":"Genesis","chapter":1,"verse":1,"text":"In the beginning God created the heavens and the earth."}],"text":"In the beginning God created the heavens and the earth.","translation_id":"darby","translation_name":"Darby Bible","translation_note":"Public Domain"} |


#### Test Cases: `test_get_chapter`
Having above test cases covering the whole responses, this test checks the length of the returned verses for different notations to assure the api works as expected.

| Test Case ID | Path            | Expected Verse Count |
|--------------|-----------------|---------------------|
| TC_04        | gen 1:2-4,6     | 4                   |
| TC_05        | gen 2           | 25                  |


#### Test Cases: `test_invalid_request`
Checking if trying to access non-existing books or chapters returns an error.

| Test Case ID | Path    | Expected Status Code |
|--------------|---------|----------------------|
| TC_06        | gen 404 | 404                  |
| TC_07        | asdf    | 404                  |
