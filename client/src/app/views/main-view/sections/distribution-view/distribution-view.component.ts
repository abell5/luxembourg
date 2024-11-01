import { AfterViewInit, Component, ElementRef, Input, ViewChild } from '@angular/core';
import { TokenDistribution } from '../../../../model/tokenDistribution.model';
import { HorizontalBarchart } from 'JCharts';

@Component({
  selector: 'app-distribution-view',
  standalone: true,
  imports: [],
  templateUrl: './distribution-view.component.html',
  styleUrl: './distribution-view.component.scss'
})
export class DistributionViewComponent implements AfterViewInit {

  protected _tokenDistribution: TokenDistribution | null = null;

  // inputs
  @Input({alias: 'tokenDistribution'})
  get tokenDistribution(): TokenDistribution | null {

    if( !this._tokenDistribution ) return null;
    return this._tokenDistribution;

  }
  set tokenDistribution(tokenDistribution: TokenDistribution | null) {    
    
    if( !tokenDistribution ) return;
    this._tokenDistribution = tokenDistribution;
  
  }

  // DOM Refs
  @ViewChild('chartcontainerref') chartContainerRef!: ElementRef;

  ngAfterViewInit(): void {
    
    let horizontalBarChartValues: number[] = Array(20).fill(0).map( (v: number) => Math.random() );
    let horizontalBarChartLabels: string[] = Array(20).fill(0).map( (v: number, index: number) => `label-${index}` );
    const horizontalBarChartDiv: HTMLDivElement = this.chartContainerRef.nativeElement;
    
    const horizontalBarchart: HorizontalBarchart = new HorizontalBarchart( 
        horizontalBarChartDiv, 
        { 
            margins: { top: 10, bottom: 40, left: 20, right: 20 }, 
            xAxisBottomParams: { visible: true, chartPadding: 5, domainStrokeWidth: 1, domainStrokeColor: "#bababa", domainLineVisibility: true, tickNumber: 3, textSize: 12 },
            brushParams: { activated: true, type: 'x' }  
        }, 
        {'end': (event: number[] | null ) => {
                console.log(event);
            }
        });

    horizontalBarchart.update( {values: horizontalBarChartValues, labels: horizontalBarChartLabels}, {domain: [0,1]} );


  }

}
