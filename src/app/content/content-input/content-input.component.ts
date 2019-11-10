import { Component, OnInit, Input } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Content } from '../../models';


@Component({
  selector: 'app-content-input',
  templateUrl: './content-input.component.html',
  styleUrls: ['./content-input.component.scss'],
})
export class ContentInputComponent implements OnInit {
  @Input() content: any;
  @Input() preview = true;
  contentForm: FormGroup;

  constructor(private formBuilder: FormBuilder) {
    console.log('I have awakened')
   }

  ngOnInit() {
    if (this.content == null) {
      this.content = {
        Title: '',
        Body: '',
        Attachments: [],
        Tags: []
      }
      this.preview = false;
    }

    this.contentForm = this.formBuilder.group({
      'Title': [this.content.Title],
      'Body': [this.content.Body]
    })
  }

}
